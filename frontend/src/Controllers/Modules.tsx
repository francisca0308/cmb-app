import ModulesList from "../Components/Modules/ModulesList";

import { useModulesData } from "../Data/modules";

export default function Modules() {
  const modules = useModulesData();
  return (
    <div>
      <h1>All modules</h1>
      <ModulesList modules_chat={modules}></ModulesList>
    </div>
  );
}
