class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = []
        
        # Create birth and death events
        for birth, death in logs:
            events.append((birth, 1))    # Birth increases population
            events.append((death, -1))   # Death decreases population
        
        # Sort events by year
        events.sort()
        
        population = 0
        max_population = 0
        best_year = 0
        
        # Sweep through events and track maximum population
        for year, change in events:
            population += change
            
            # Update only if we found a strictly greater population
            # This ensures we get the earliest year with max population
            if population > max_population:
                max_population = population 
                best_year = year
                
        return best_year