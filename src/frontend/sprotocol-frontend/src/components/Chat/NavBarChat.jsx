function NavBarChat() {
    return (
        <>

            <nav className="navbar h-10 ">
                <div className="container-fluid">
                    <a className="navbar-brand d-flex align-items-center justify-content-center" href="#">
                        <div className="sender ms-2 bg-warning">Sender Name </div>
                        <div className="recevier ms-2 bg-success">recevier Name</div>
                    </a>

                    <div className="d-flex me-4">
                        <button type="button" className="btn btn-danger ">
                            <span className="bedge small m-2"> <img src="../../../assets/stopwatch.svg" alt="stopwatch svg" /> </span>
                            Stop
                        </button>
                    </div>
                </div>

            </nav>

        </>
    );
}


export default NavBarChat