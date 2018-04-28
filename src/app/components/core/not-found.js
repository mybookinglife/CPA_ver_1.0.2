import { Link } from 'react-router';
import { URL } from "../../constants/config";

export default function NotFound(props) {

        return(<div>Страница не найдена. Вернуться на <Link to={URL}>главную</Link></div>);

}