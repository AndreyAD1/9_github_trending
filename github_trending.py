import requests
import datetime


def get_first_date_of_request(days_number):
    current_date = datetime.date.today()
    time_gap = datetime.timedelta(days=days_number)
    first_date_of_request = (current_date - time_gap)
    return first_date_of_request


def get_sorted_repos_created_after_a_date(filter_date):
    github_repos_url = 'https://api.github.com/search/repositories'
    creation_date_argument = 'created:>={}'.format(filter_date)
    request_arguments = {'q': creation_date_argument, 'sort': 'stars'}
    try:
        all_repos_request = requests.get(
            github_repos_url,
            params=request_arguments
        )
        return all_repos_request.json()
    except requests.exceptions.RequestException:
        return None


def get_most_popular_repositories(all_repositories, output_repos_number):
    all_repos_number = all_repositories['total_count']
    if all_repos_number < output_repos_number:
        output_repos_number = output_repos_number
    most_popular_repositories = all_repositories['items'][:output_repos_number]
    return most_popular_repositories


def print_repositories(repo_list):
    print('Most popular repositories created this week:')
    for repository in repo_list:
        repo_url = repository['html_url']
        repo_stars = repository['stargazers_count']
        repo_issues = repository['open_issues']
        print('URL: {}, stars: {}, open issues: {}'.format(
            repo_url,
            repo_stars,
            repo_issues
        ))


if __name__ == '__main__':
    days_before_today = 7
    request_beginning_date = get_first_date_of_request(days_before_today)
    all_repos_info = get_sorted_repos_created_after_a_date(
        request_beginning_date
    )
    if not all_repos_info:
        exit('Can not get data from api.github.com.')
    max_number_of_repos = 20
    trending_repositories = get_most_popular_repositories(
        all_repos_info, max_number_of_repos
    )
    print_repositories(trending_repositories)
