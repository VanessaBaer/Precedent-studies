# Stubbed utils for local replication (no network)

def graphql_query(query: str, variables: dict | None = None):
    return {
        "data": {
            "repository": {
                "pullRequest": {
                    "title": "feat(api): add users (JIRA-456)"
                }
            }
        }
    }

def is_author_a_bot(repo_list: list[str], pull_request_id: int) -> bool:
    return False
