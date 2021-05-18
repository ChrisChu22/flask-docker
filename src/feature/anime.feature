Feature: Anime Title
  As anime watcher,
  I want to know the title of the show.


  Scenario Outline: Anime Name
    When the Anime API is queried with "<number>"
    Then the response status code is 200
    And the response shows title of "<title>"

    Examples: Anime Names
      | number          | title       |
      | 1               | Cowboy Bebop|
      | 64              | Rozen Maiden|
      | 99              | Mai-Otome   |