import "./modules.css";
import ModuleDisplay from "./ModuleDisplay";

import { Module } from "../../Data/modules";

interface Props {
  modules_chat: Module[];
}

export default function ModulesList({ modules_chat }: Props) {
  return (
    <div className="module-list">
      {modules_chat.map((module) => (
        <ModuleDisplay key={module.id} module={module} />
      ))}
    </div>
  );
}
