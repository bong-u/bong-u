import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { Quote } from './quote'
import { Project } from './project'
import { Career } from './career'

ReactDOM.render(
	<div id="pages">
		<Quote/>
		<Project/>
		<Career/>
	</div>,
	document.getElementById('root')
);
