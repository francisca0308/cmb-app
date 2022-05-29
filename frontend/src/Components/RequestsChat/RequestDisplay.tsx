import "./request.css";
import { RequestChat } from "../../Data/requests";

interface Props {
  request: RequestChat;
}

export function RequestDisplay({ request }: Props) {
  return (
    <>
      <tr>
        <td className="module-element">Solicitante {request.person_id}</td>
        <td>{request.module_id}</td>
        <td>{request.comment}</td>
        <td>{request.initial_date}</td>
        <td>
          <button>Aceptar</button>
        </td>
      </tr>
    </>
  );
}

export default RequestDisplay;
