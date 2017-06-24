import MenuComponent from './menu-component';
export default function MainComponentLayout(props) {

    return (
        <div className="container-fluid">
            <div className="row">
               <footer>
                   {MenuComponent(props)}
               </footer>
            </div>
            <div className="row">
               <main>
                   {props.children}
               </main>
            </div>
        </div>);
}