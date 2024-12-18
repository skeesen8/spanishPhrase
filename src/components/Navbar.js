import React from "react";
import Home from "./Home";
import { Link } from 'react-router-dom';

function Navbar(){
    return(
        <nav>
            <Link to="/home">Home</Link>
        </nav>
    )
}

export default Navbar