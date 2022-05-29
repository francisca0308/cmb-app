import { Link } from "react-router-dom";
import { useModulesData } from "../Data/modules";
import {
  MODULES_LINK,
  REQUESTS_LINK,
  CALENDAR_LINK,
} from "../Navigation/routes";
import "./Styles/home.css";

export default function Home() {
  const modules_chat = useModulesData();
  console.log(modules_chat);

  return (
    <>
      <div className="home">
        <h3> ¡BIENVENID@ A CMB! </h3>
        <p>Un lugar donde puedes intercambiar tus turnos de Chat fácilmente</p>
        <div className="links">
          <div className="button">
            <Link to={`${MODULES_LINK}`}>Modulos</Link>
          </div>
          <div className="button">
            <Link to={`${REQUESTS_LINK}`}>Solicitudes</Link>
          </div>
          <div className="button">
            <Link to={`${CALENDAR_LINK}`}>Mi calendario</Link>
          </div>
        </div>
      </div>
    </>
  );
}
