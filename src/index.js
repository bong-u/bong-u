import React from 'react';
import ReactDOM from 'react-dom';
import './style.css';

class Quote extends React.Component {
	render() {
		return (
			<div id='text'>“Talk is cheap. Show me the code.”
― Linus Torvalds</div>
		);
	}
}

class Content extends React.Component {

	render() {
		return (
			<div>
				<div className="project">
					<span>Tetris</span>
				</div>
				<div className="project">
					<span>MineSweeper</span>
				</div>
			</div>
		);
	}
}

ReactDOM.render(
	<div>
		<Quote/>
		<Content/>
	</div>,
	document.getElementById('root')
);
