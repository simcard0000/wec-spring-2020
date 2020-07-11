/** @format */

import React, { useRef } from "react";
import { Button, InputGroup, Card, Elevation } from "@blueprintjs/core";
import { IconNames } from "@blueprintjs/icons";
import "./App.css";

function App() {
  const searchInput = useRef(null);
  const removeWebsite = useRef(null);
  const findWebsite = useRef(null);
  const onSearchClick = () => {
    
  };
	const SearchButton = (
		<Button intent="success" icon={IconNames.SEARCH} onClick={onSearchClick()}>
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
			    <div className="left-options-body" >
			        <h5>Remove from Query</h5>
			        <InputGroup
			            className="options-field"
			            defaultValue=""
			            placeholder="URLS separated by commas"
			            ref={removeWebsite}
			        />
			    </div>
			    <div className="right-options-body" >
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
