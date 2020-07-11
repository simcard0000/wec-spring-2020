/** @format */

import React, { useRef } from "react";
import { Button, InputGroup, Card, Elevation } from "@blueprintjs/core";
import { IconNames } from "@blueprintjs/icons";
import "./App.css";

function App() {
  const searchInput = useRef(null);
  const SearchButton = <Button intent="success" icon={IconNames.SEARCH}>Search</Button>;
	return (
		<div className="main">
			<div className="title-header">
				<img className="title-icon" src="book.svg" />
				<h1 padding="0px">Mini Engine</h1>
			</div>
			<p>What are you looking for?</p>
			<div className="search-body">
				<InputGroup
					className="search-bar"
					defaultValue="search here!"
          ref={searchInput}
          rightElement={SearchButton}
				/>
			</div>
      <div className="results-body">
        //in that list of dictionaries, get the length and print.
        <Card id="" interactive="true"></Card>
      </div>
		</div>
	);
}

export default App;
