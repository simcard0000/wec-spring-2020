/** @format */

import React, { useRef, useEffect } from "react";
import { Button, InputGroup, Card, Elevation } from "@blueprintjs/core";
import { IconNames } from "@blueprintjs/icons";
import "./App.css";

function App() {
	const removeWebsite = useRef(null);
	const findWebsite = useRef(null);
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
					defaultValue=""
					placeholder="search here!"
					ref={searchInput}
					rightElement={SearchButton}
				/>
			</div>

			<br></br>

			<div className="options-body">
				<h3 class="h3-general">Advanced Options:</h3>
				<div className="left-options-body">
					<h5>Remove from Query</h5>
					<InputGroup
						className="options-field"
						defaultValue=""
						placeholder="URLS separated by commas"
						ref={removeWebsite}
					/>
				</div>
				<div className="right-options-body">
					<h5>Find from Query</h5>
					<InputGroup
						className="options-field"
						defaultValue=""
						placeholder="URLS separated by commas"
						ref={findWebsite}
					/>
				</div>
			</div>

			<br></br>

			<div className="results-body">
				<Card className="results-card" id="" interactive="true">
					<h2>Calculus III - Triple Integrals</h2>
					<h3>
						<a href="https://tutorial.math.lamar.edu/classes/calciii/tripleintegrals.aspx">
							link
						</a>
					</h3>
					<h4>
						'Jun 1, 2018 ... Section 4-5 : Triple Integrals. Now that we know
						how to integrate over a two-\ndimensional region we need to move on
						to integrating over a\xa0...'
					</h4>
				</Card>
			</div>
		</div>
	);
}

export default App;
