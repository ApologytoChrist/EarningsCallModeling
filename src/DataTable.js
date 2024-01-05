import React, {useEffect, useState} from "react";
import './DataTable.css'
function DataTable () {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/data')
            .then((response) => response.json())
            .then((data) => setData(data))
            .catch((error) => console.error('Error fetching data', error));
    }, []);


    return (
        <table>
            <thead>
            <tr>
                <th>Date</th>
                <th>Time of Day</th>
                <th>Ticker</th>
                <th>Prior EPS</th>
                <th>Estimated EPS</th>
                <th>Estimated EPS Growth</th>
                <th>Actual EPS</th>
                <th>Prior Rev</th>
                <th>Estimated Rev Growth</th>
                <th>Actual Rev</th>

            </tr>
            </thead>
            <tbody>
            {data.slice(0, data.length).map((item, index) => {
                return (
                    <tr>
                        <td>{item[0]}</td>
                        <td>{item[1]}</td>
                        <td>{item[2]}</td>
                        <td>{item[3]}</td>
                        <td>{item[4]}</td>
                        <td>{item[5]}%</td>
                        <td>{item[6]}</td>
                        <td>{item[7]}</td>
                        <td>{item[8]}</td>
                        <td>{item[9]}</td>
                    </tr>
                );
            })}
            </tbody>
        </table>
    );
}

export default DataTable