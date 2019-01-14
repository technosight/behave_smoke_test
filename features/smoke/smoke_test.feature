Feature: Simple smoke test
  Print Hello World!

  @test
  Scenario: Print the popular greeting
    Given print start notice I'm starting
    Then print preparedness notice I'm ready
    Then print greeting Hello World!