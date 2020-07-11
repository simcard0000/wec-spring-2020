/** @format */

import React, { useRef, useEffect } from "react";
import { Button, InputGroup, Card, Elevation } from "@blueprintjs/core";
import { IconNames } from "@blueprintjs/icons";
import "./App.css";

function App() {
	const searchInput = useRef(null);
	let resultsArray = [];
	const onSearchClick = () => {
		if (searchInput.current != null) {
			fetch("/search?query=Hello", {
        method: "GET",
			}).then(function (response) {
				if (response.ok) {
					console.debug(response.json());
				}
				//return response.json();
			});
		}
	};
	const SearchButton = (
		<Button intent="success" icon={IconNames.SEARCH} onClick={onSearchClick}>
			Search
		</Button>
	);
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
			<br></br>
			<div className="results-body">
				<Card className="results-card" id="" interactive="true">
					<h2>title</h2>
					<h3>
						<a href="">link</a>
					</h3>
					<h4>snippet</h4>
				</Card>
			</div>
		</div>
	);
}

export default App;
