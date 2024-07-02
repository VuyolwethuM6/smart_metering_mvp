import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
    const [usageData, setUsageData] = useState([]);
    const [goal, setGoal] = useState(100); // Example goal
    const [alert, setAlert] = useState(false);

    useEffect(() => {
        axios.get('/usage')
            .then(response => {
                console.log(response.data);  // Check fetched data in console
                setUsageData(response.data);
            })
            .catch(error => console.error(error));
    }, []);

    useEffect(() => {
        const totalUsage = usageData.reduce((acc, data) => acc + data.usage, 0);
        if (totalUsage > goal) {
            setAlert(true);
        } else {
            setAlert(false);
        }
    }, [usageData, goal]);

    return (
        <div>
            <h1>Electricity Usage Dashboard</h1>
            {alert && <p style={{ color: 'red' }}>You are close to reaching your usage goal!</p>}
            <ul>
                {usageData.map(data => (
                    <li key={data.timestamp}>
                        {data.timestamp}: {data.usage.toFixed(2)} kWh
                    </li>
                ))}
            </ul>
            <div>
                <label>
                    Set Usage Goal (kWh):
                    <input type="number" value={goal} onChange={(e) => setGoal(e.target.value)} />
                </label>
            </div>
        </div>
    );
}

export default App;
