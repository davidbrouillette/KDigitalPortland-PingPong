import React from 'react';
import Score from './score.js';
import ServeIndicator from './scoreIndicator.js';
import { Server } from 'http';

const PlayerInfo = ({}) => {
	return (
		<div className="player-info-component">
			<div className="section-score">
				<Score scoreToDisplay={0} />
			</div>
			<div className="section-serve-indicator">
				<ServeIndicator 
					indicator="-->"
					active={true} />
			</div>
			
		</div>
	)
}

export default PlayerInfo;
