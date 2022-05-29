import RequestDisplay from "../Components/RequestsChat/RequestDisplay";

import { useRequestData } from "../Data/requests";

export default function Requests() {
  const requests = useRequestData();
  return (
    <div>
      <h1>All requests</h1>
      <table>
        <tr>
          <th>Solicitante</th>
          <th>Modulo</th>
          <th>Comentario</th>
          <th>Fecha</th>
        </tr>
        {requests.map((request) => (
          <RequestDisplay key={request.id} request={request} />
        ))}
      </table>
    </div>
  );
}
