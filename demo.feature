Feature: AnimeFLV

 Scenario: el ultimo episodio es el 999
   Given chrome is up
   When the user gets animeflv page
   And the user clicks one piece link
   Then The last episode is 999