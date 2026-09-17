"""Busca o histórico de contribuições de um usuário do GitHub via GraphQL."""

import os
import requests

GRAPHQL_URL = "https://api.github.com/graphql"

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""


def get_token() -> str:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError(
            "Defina a variável de ambiente GITHUB_TOKEN com um Personal "
            "Access Token (escopo read:user)."
        )
    return token


def fetch_contributions(username: str) -> list[list[int]]:
    """Retorna uma matriz [semana][dia] com a contagem de contribuições."""
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(
        GRAPHQL_URL,
        json={"query": QUERY, "variables": {"login": username}},
        headers=headers,
        timeout=15,
    )
    response.raise_for_status()
    data = response.json()

    if "errors" in data:
        raise RuntimeError(f"Erro da API do GitHub: {data['errors']}")

    weeks = data["data"]["user"]["contributionsCollection"][
        "contributionCalendar"
    ]["weeks"]

    grid = []
    for week in weeks:
        days = [day["contributionCount"] for day in week["contributionDays"]]
        # preenche semanas incompletas (início/fim do período) com zero
        while len(days) < 7:
            days.append(0)
        grid.append(days)

    return grid
