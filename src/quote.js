import React from 'react';
import './quote.css';

class Quote extends React.Component {
	render() {
		return (
			<div id='quote'>
				<div>
					<p>“Simplicity is prerequisite for reliability.” - Edsger Dijkstra</p>
				</div>
			</div>
		);
	}
}

export { Quote };