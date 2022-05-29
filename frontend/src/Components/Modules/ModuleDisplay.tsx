import "./modules.css";
import { Module } from "../../Data/modules";

interface Props {
  module: Module;
}

export function ModuleDisplay({ module }: Props) {
  return (
    <>
      <div
        className={`module-root ${
          module.state == 0 ? "green" : module.state == 1 ? "yellow" : "red"
        }`}
      >
        <div className="module-element">Modulo {module.id}</div>
        <div>{module.initial_date}</div>
        <div>{module.people}</div>
      </div>
    </>
  );
}

export default ModuleDisplay;
