import React from 'react';
import Layout from './layout';

class App extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
            <div className="app-component-container">
                <Layout />
            </div>
        )
    }
}

export default App;