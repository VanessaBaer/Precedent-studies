from utils.github import graphql_query, is_author_a_bot
import sys
import re

for index, arg in enumerate(sys.argv):
    if index == 0:
        continue
    elif arg == "--repository-name":
        repository_name = sys.argv[index + 1]
        sys.argv.pop(index)
    elif arg == "--pull-request-id":
        pull_request_id = int(sys.argv[index + 1])
        sys.argv.pop(index)
    elif arg == "--regex":
        regex_string = sys.argv[index + 1]
        sys.argv.pop(index)
    else:
        raise Exception(f"Unknown argument {arg}")

repo_list = repository_name.split("/")

if is_author_a_bot(repo_list=repo_list, pull_request_id=pull_request_id):
    print("author is a bot, skipping.")
    exit(0)

pull_request_title_query = f"""
{{
  repository(owner: "{repo_list[0]}", name: "{repo_list[1]}") {{
    pullRequest(number: {pull_request_id}) {{
      title
    }}
  }}
}}
"""

pull_request_title_data = graphql_query(query=pull_request_title_query)
print(pull_request_title_data["data"]["repository"]["pullRequest"]["title"])

res = re.search(
    regex_string, pull_request_title_data["data"]["repository"]["pullRequest"]["title"]
)

if res is None:
    print(f"Invalid PR Title, must match {regex_string}")
    exit(1)
else:
    exit(0)
