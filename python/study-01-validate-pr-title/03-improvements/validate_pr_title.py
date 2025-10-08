import argparse
import re
import sys
from utils.github import graphql_query, is_author_a_bot

def parse_args():
    p = argparse.ArgumentParser(description="Validate a PR title against a regex.")
    p.add_argument("--repository-name", required=True, help="Format: owner/repo")
    p.add_argument("--pull-request-id", required=True, type=int)
    p.add_argument("--regex", required=True, help="Python regex to match PR title")
    p.add_argument("--full-match", action="store_true",
                   help="Anchor the regex to match the entire title (^...$)")
    p.add_argument("--ignore-case", action="store_true",
                   help="Case-insensitive regex match")
    p.add_argument("--no-bot-skip", action="store_true",
                   help="Validate even if author is a bot")
    return p.parse_args()

def main():
    args = parse_args()

    try:
        owner, name = args.repository_name.split("/", 1)
    except ValueError:
        print("Error: --repository-name must be in the form owner/repo", file=sys.stderr)
        return 2

    try:
        if not args.no_bot_skip and is_author_a_bot(
            repo_list=[owner, name],
            pull_request_id=args.pull_request_id
        ):
            print("author is a bot, skipping.")
            return 0
    except Exception as e:
        print(f"Error checking author bot status: {e}", file=sys.stderr)
        return 2

    pattern_str = args.regex
    if args.full_match and not (pattern_str.startswith("^") and pattern_str.endswith("$")):
        pattern_str = f"^{pattern_str}$"

    flags = re.IGNORECASE if args.ignore_case else 0
    try:
        pattern = re.compile(pattern_str, flags)
    except re.error as e:
        print(f"Invalid regex: {e}", file=sys.stderr)
        return 2

    query = """
    query($owner:String!, $name:String!, $number:Int!) {
      repository(owner: $owner, name: $name) {
        pullRequest(number: $number) {
          title
          number
        }
      }
    }
    """
    variables = {"owner": owner, "name": name, "number": args.pull_request_id}

    try:
        data = graphql_query(query=query, variables=variables)
    except Exception as e:
        print(f"GraphQL request failed: {e}", file=sys.stderr)
        return 2

    if not data or "data" not in data or data.get("errors"):
        print(f"GraphQL error: {data.get('errors') if isinstance(data, dict) else 'unknown'}",
              file=sys.stderr)
        return 2

    pr = (data["data"].get("repository") or {}).get("pullRequest")
    if not pr:
        print("Pull request not found.", file=sys.stderr)
        return 2

    title = pr.get("title", "")
    print(title)

    if pattern.search(title) is None:
        print(f"Invalid PR Title, must match {pattern.pattern}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
