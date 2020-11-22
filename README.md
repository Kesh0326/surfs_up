# Surfs_up Challenge

## Analysis Overview
Analytics on temperature data for the months of June and December to help an upcoming surf-shake store understand weather patterns in Oahu to decide whether it's worth investing in the venture

## Analysis Results
Based on the temperature findings for June and December, the following can be observed

- The average temperature observed during the month of June is 75F while the average temperature for December is lower at 71F indicating that June is a warmer month and may be considered more conducive for surfing and milkshakes
- The maximum recorded temperature in June is 85F while the maximum temperature for December is 83F indicating there isn't that significant of a difference in maximum temperature across both months 
- The minimum temperature observed in June is 64F while that in December is 56F indicating that there can be days in December that are less favorable (colder) to surfing and shakes than in June

## Analysis Summary
Based on the analysis, it can be noticed that in June the most frequently observed temperatures lie between 72 - 79F and in December, the most frequently observed temperatures lie between 67 - 75F indicating that there isn't a large fluctuation in temperatures in Oahu across both months and based on temperature alone, it can be inferred that the location can be condusive to set up a surf-shake shop that can be a profitable venture all year round

However, additional parameters would can help make a more conclusive inference between June and December

1) results_june = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==6).all() 

The query above can help understand what the precipitation levels are across both of these months (indicated for June above - replace 6 with 12 to get preciptation levels for December) and get a better sense of climate

2) session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()

The query above can be used to identify the most active stations where the temperature was observed and can be used to map station status vs. number of observations recorded to ensure data is being used from active stations
