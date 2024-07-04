## Project Requirements Document for Famous Investors

### Unit Tests

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The index view must handle GET requests correctly. | When a GET request is made to the index URL. | The response should have a status code of 200 and use the index.html template. The response must contain the text 'Famous Investors'. | test_index_get
The index URL should resolve correctly to the HomeView. | When the index URL is resolved. | The resolved URL should map to views.HomeView. | test_index_url_is_resolved
The utility must correctly calculate the average population. | When querying population data from multiple countries. | The population average should be 175,000,000. | test_uitilities, assertEquals(data.population_avg, 175000000)
The utility must correctly calculate the average age of investors. | When querying age data from multiple investors. | The age average should be 37. | test_uitilities, assertEquals(data.age_avg, 37)
The utility must correctly calculate the average AUM. | When querying AUM data from multiple funds. | The AUM average should be 200,000,000. | test_uitilities, assertEquals(data.aum_avg, 200000000)
The utility must correctly identify the type of market for the first fund. | When querying market data from multiple funds. | The first fund's market type should be 'bonds'. | test_uitilities, assertEquals(data.funds[0], 'bonds')
