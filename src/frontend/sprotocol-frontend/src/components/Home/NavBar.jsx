function NavBar() {
    return (
        <>

            <nav className="navbar navbar-expand-lg">
                <div className="container-fluid">
                    <a className="navbar-brand" href="#">
                        <img src="./././assets/sprotocol-logos/sprotocol-logos_black.png" alt="Logo" width="120" height="120" className="d-inline-block align-text-top" />

                    </a>

                    <div className="d-flex me-4">

                        <a href="https://github.com/saad-als/sprotocol" className=" rounded">
                            <img src="./././assets/github-mark.png" width="35" height="35" alt="a github logo" />
                        </a>
                    </div>
                </div>

            </nav>
        </>
    );
}

export default NavBar