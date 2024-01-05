import './App.css';
import React, {useEffect, useState} from "react";
import DataTable from './DataTable'
import './DataTable.css'
function App() {

  return (
    <div className="App">
        <DataTable data={DataTable.data} />
    </div>
  );
}


export default App;

