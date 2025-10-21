// Update parking data every 2 seconds
setInterval(updateParkingData, 2000);

async function updateParkingData() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();
        
        // Update statistics
        document.getElementById('available-spots').textContent = data.statistics.available || 0;
        document.getElementById('occupied-spots').textContent = data.statistics.occupied || 0;
        document.getElementById('total-spots').textContent = data.statistics.total || 0;
        
        // Update timestamp
        document.getElementById('timestamp').textContent = new Date(data.timestamp).toLocaleTimeString();
        
        // Update parking spots
        updateParkingSpots(data.status);
        
    } catch (error) {
        console.error('Error fetching parking data:', error);
    }
}

function updateParkingSpots(spots) {
    const parkingGrid = document.getElementById('parking-grid');
    parkingGrid.innerHTML = '';
    
    spots.forEach(spot => {
        const spotElement = document.createElement('div');
        spotElement.className = 'parking-spot';
        
        const statusClass = spot.occupied ? 'status-occupied' : 'status-available';
        const statusText = spot.occupied ? 'Occupied' : 'Available';
        
        spotElement.innerHTML = `
            <div class="spot-info">
                <span class="spot-name">${spot.name}</span>
                <span class="spot-type">${spot.type}</span>
            </div>
            <div class="spot-status ${statusClass}">${statusText}</div>
        `;
        
        parkingGrid.appendChild(spotElement);
    });
}

// Initial load
updateParkingData();
