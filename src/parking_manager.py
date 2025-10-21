"""
Parking spot management and occupancy detection
"""

class ParkingManager:
    def __init__(self, parking_spots):
        self.parking_spots = parking_spots
        self.occupancy_history = []
    
    def check_spot_occupancy(self, spot, detected_cars):
        """Check if a parking spot is occupied"""
        spot_coords = spot['coords']
        
        for car in detected_cars:
            if self._check_overlap(spot_coords, car[:4]):  # x1,y1,x2,y2
                return True
        return False
    
    def _check_overlap(self, spot, car_bbox):
        """Check if car bounding box overlaps with parking spot"""
        spot_x1, spot_y1, spot_x2, spot_y2 = spot
        car_x1, car_y1, car_x2, car_y2 = car_bbox
        
        # Простая проверка пересечения
        overlap_x = max(0, min(spot_x2, car_x2) - max(spot_x1, car_x1))
        overlap_y = max(0, min(spot_y2, car_y2) - max(spot_y1, car_y1))
        overlap_area = overlap_x * overlap_y
        
        spot_area = (spot_x2 - spot_x1) * (spot_y2 - spot_y1)
        
        # Считаем занятым если перекрытие > 30% площади места
        return (overlap_area / spot_area) > 0.3
    
    def get_parking_status(self, detected_cars):
        """Get current status of all parking spots"""
        status = []
        
        for spot in self.parking_spots:
            occupied = self.check_spot_occupancy(spot, detected_cars)
            status.append({
                'id': spot['id'],
                'name': spot['name'],
                'type': spot['type'],
                'occupied': occupied,
                'coords': spot['coords']
            })
            
        self.occupancy_history.append(status)
        return status
    
    def get_statistics(self):
        """Get parking statistics"""
        if not self.occupancy_history:
            return {}
            
        current_status = self.occupancy_history[-1]
        occupied_count = sum(1 for spot in current_status if spot['occupied'])
        total_count = len(current_status)
        
        return {
            'occupied': occupied_count,
            'available': total_count - occupied_count,
            'total': total_count,
            'occupancy_rate': occupied_count / total_count if total_count > 0 else 0
        }
