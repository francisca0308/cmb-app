import ModulesList from "../Components/Modules/ModulesList";
import "./Styles/calendar.css";

import { useModulesData } from "../Data/modules";

export default function Calendar() {
  const modules = useModulesData();
  return (
    <div className="calendar">
      <h1>My Preferences</h1>
      <div className="days">
        <p>Lunes</p>
      </div>
      <ModulesList modules_chat={modules}></ModulesList>
    </div>
  );
}
