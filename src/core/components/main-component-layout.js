export default function MainComponentLayout(props) {

    return (
        <div className="container-fluid">
            <div className="row">
               <footer>
                   {props.menu}
               </footer>
            </div>
            <div className="row">
               <main>
                   {props.children}
               </main>
            </div>
        </div>);
}