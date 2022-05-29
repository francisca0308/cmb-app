import "./navbar.css";
import { Link } from "react-router-dom";

export default function NavBar() {
  return (
    <div className="navbar-root">
      <div className="navbar-menu">
        <div>
          <Link to="/">
            <img
              className="navbar-img"
              src={require("../../../Assets/Logo_de_Fintual.png")}
              alt="myMarketIcon"
            ></img>
          </Link>
        </div>
      </div>
      <div className="title">
        <h1>CMB</h1>
      </div>
      <div>
        <img
          className="navbar-img"
          src={require("../../../Assets/user.png")}
          alt="cartIcon"
        ></img>
      </div>
    </div>
  );
}
