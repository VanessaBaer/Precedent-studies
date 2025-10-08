from utils.github import graphql_query, is_author_a_bot
import sys
import re

# --- Argument parsing (simple, matches the baseline logic) ---
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

# --- Core logic ---
repo_list = repository_name.split("/")

# Simulate bot check (stubbed in utils/github.py)
if is_author_a_bot(repo_list=repo_list, pull_request_id=pull_request_id):
    print("author is a bot, skipping.")
    exit(0)

# Stubbed GraphQL call (returns data from local utils/github.py or fixture)
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

# Extract title from the stubbed GraphQL response
title = pull_request_title_data["data"]["repository"]["pullRequest"]["title"]
print(title)

# --- Regex validation ---
res = re.search(regex_string, title)

if res is None:
    print(f"Invalid PR Title, must match {regex_string}")
    exit(1)
else:
    exit(0)
