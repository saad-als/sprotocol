function NavBar() {
    return (
        <>

            <nav className="navbar h-10">
                <div className="container-fluid">
                    <a className="navbar-brand" href="#">
                        <img src="./././assets/sprotocol-logos/sprotocol-logos_black.png" alt="Logo" width="120" height="120" className="d-inline-block align-text-top" />

                    </a>

                    <div className="d-flex me-4">
                        <div className="dropdown">
                            <button className="btn btn-light dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                <span className="navbar-toggler-icon"></span>
                            </button>
                            <ul className="dropdown-menu">
                                <li><a className="dropdown-item" href="#">Dark theme</a></li>
                                <li><a className="dropdown-item" href="#">Github</a></li>
                            </ul>
                        </div>
                    </div>
                </div>

            </nav>
        </>
    );
}

export default NavBar