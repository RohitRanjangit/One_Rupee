import React, { Component } from "react";
import "./App.css";
import SideBar from "./components/sidebar/sidebar";
import TopBar from "./components/topbar/topbar";
import Main from "./components/main";
import {BrowserRouter as Router,Switch,Route} from "react-router-dom"
class App extends Component {
  constructor() {
    super();
    this.state = {
      pages: [
        { name: "Profile", icon: "user" ,route:"/profile"},
        { name: "Home", icon: "home" ,route:"/feed" },
        { name: "Request", icon:"money",route:"/request" },
        { name: "Leaderboard", icon: "trophy",route:"/leaderboard" },
        { name: "History", icon: "history",route:"/history" },
        { name: "Landing", icon: "",route:"/" },
        { name: "Registration",icon: "",route:"/registration"}
      ],
      isNgo: false,
      token:"",
      pk:0,
      activePage: 5,
      sidebarActive: true,
      profilePic: "https://docs.atlassian.com/aui/8.3.1/docs/images/avatar-person.svg"
    };
  }

  sidebarToggleHandler = () => {
    this.setState({ sidebarActive: !this.state.sidebarActive });
  };

  changeToken=(value)=>{
    this.setState({token:value})
  }
  
  changePk = value=>{
    this.setState({pk:value})
  }

  setType = value=>{
    this.setState({isNgo:value})
  }

  switchPage = page => {
    const newActive = this.state.pages.findIndex(pg => pg.name === page.name);
    this.setState({ activePage: newActive });
    console.log(this.state.pages[this.state.activePage].route)
  };

  changePic = path => {
    this.setState({profilePic: path})
  }

  render() {
    const active= this.state.token==="" ? false : this.state.sidebarActive
    const Ab = () =>{
      return(
        <Main
        page={this.state.pages[this.state.activePage]}
        sidebarActive={active}
        pageHandler={this.switchPage}
        pages= {this.state.pages}
        pic={this.state.profilePic}
        changePic={this.changePic}
        changeToken={this.changeToken}
        token={this.state.token}
        pk={this.state.pk}
        changePk={this.changePk}
        isNgo={this.state.isNgo}
        setType={this.setType}
      /> 
      )
    }
    // if(this.state.activePage===5) 
    // return (
    //   <Router><Switch>
    //    <Route path={this.state.activePage.route} exact component ={Ab}/>  
    //   </Switch></Router>
    // )
    // else
    return (
      <Router><Switch><React.Fragment>
      <TopBar
        onSidebarToggle={this.sidebarToggleHandler}
        active={this.state.sidebarActive}
        currentPage={this.state.pages[this.state.activePage]}
        token={this.state.token}
        changeToken={this.changeToken}
        pk={this.state.pk}
        changePk={this.changePk}
        isNgo={this.state.isNgo}
        setType={this.setType}
      />
      <SideBar
        pages={this.state.pages}
        activePage={this.state.activePage}
        pageHandler={this.switchPage}
        active={active}
        profilePic = {this.state.profilePic}
        token={this.state.token}
        changeToken={this.changeToken}
        pk={this.state.pk}
        changePk={this.changePk}
        isNgo={this.state.isNgo}
        setType={this.setType}
      />
      {/* Container for the main body */}
      <Route path={this.state.activePage.route} exact component ={Ab}/>
      {/* <Main
        page={this.state.pages[this.state.activePage]}
        sidebarActive={this.state.sidebarActive}
      /> */}
    </React.Fragment></Switch></Router>

      
    );
  }
}

export default App;
