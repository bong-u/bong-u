import React from 'react';
import './career.css';

class Career extends React.Component {

	render() {
		return (
			<div id="career">
				<div>
					
					<div className="item">
						<span className="date">20.05.30</span>
						<span className="content">Participated DevDay Algorithm Competition.</span>
					</div>
					<div className="item">
						<span className="date">20.07.05 ~ 20.07.25</span>
						<span className="content">Participated ARGOS club system hacking training.</span>
					</div>
					<div className="item">
						<span className="date">20.09.26</span>
						<span className="content">Participated The 4th Thinking Programming Competition.</span>
					</div>
					<div className="item">
						<span className="date">21.12.23</span>
						<span className="content">2020 crawler dataton competition - The grand prize</span>
					</div>
				</div>
			</div>
		);
	}
}


export { Career };