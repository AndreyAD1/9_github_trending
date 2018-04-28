import requests
import datetime


def get_date_before_today(days_number):
    current_date = datetime.date.today()
    time_gap = datetime.timedelta(days=days_number)
    date_before = (current_date - time_gap)
    return date_before


def get_sorted_repos_created_after_a_date(first_date_of_request):
    github_repos_url = 'https://api.github.com/search/repositories'
    creation_date_argument = 'created:>={}'.format(first_date_of_request)
    request_arguments = {'q': creation_date_argument, 'sort': 'stars'}
    try:
        repository_response = requests.get(
            github_repos_url,
            params=request_arguments
        )
        repository_info = repository_response.json()['items']
        return repository_info
    except requests.exceptions.RequestException:
        return None


def get_open_issues_of_repositories(repository_list):
    for repository in repository_list:
        repository_full_name = repository['full_name']
        server_response = requests.get(
            'https://api.github.com/repos/{}/issues'.format(
                repository_full_name
            )
        )
        open_issues_list = server_response.json()
        open_issues_number = len(open_issues_list)
        repository['open_issues_number'] = open_issues_number
    return repository_list


def print_repository_info(repository_list):
    print('Most popular repositories created this week:')
    for repository in repository_list:
        repository_url = repository['html_url']
        repository_stars = repository['stargazers_count']
        repository_issues = repository['open_issues_number']
        print('{}, stars: {}, open issues: {}'.format(
            repository_url,
            repository_stars,
            repository_issues
        ))


if __name__ == '__main__':
    days_before_today = 7
    date_before_today = get_date_before_today(days_before_today)
    all_repos_info = get_sorted_repos_created_after_a_date(
        date_before_today
    )
    if not all_repos_info:
        exit('Can not get data from api.github.com.')
    max_number_of_repos = 20
    trending_repositories = all_repos_info[:max_number_of_repos]
    repositories_with_issues_number = get_open_issues_of_repositories(
        trending_repositories
    )
    print_repository_info(trending_repositories)
