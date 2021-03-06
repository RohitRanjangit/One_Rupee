import React from "react";
import Header from "./header.js";
import Login from "./login.js";
import Footer from "./footer.js";

function Landing(props) {
  console.log(props)
  return (
    <div>
      <Header />
      <span>
        <Login token={props.token} changeToken={props.changeToken} pk={props.pk} changePk={props.changePk} isNgo={props.isNgo} setType={props.setType}/>
        <Footer />
      </span>
    </div>
  );
}
export default Landing;
