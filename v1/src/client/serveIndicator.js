import React from 'react'

const ServeIndicator = ({indicator, active}) => {
	return (
		<div className="serve-indicator-component">
			<div className={active ? "current-serve default" : "default"}>
				{ indicator }
			</div>
		</div>
	)
}

export default ServeIndicator;
