function ReceiverForm() {
    return (
        <>
            <div className="recevier-class">

                <form action="">
                    <div className="form-floating mb-3">
                        <input type="text" className="form-control" id="floatingInput" placeholder="..." />
                        <label htmlFor="floatingInput">Your Name</label>

                        <div className="d-inline-flex gap-3 m-2 form-floating">
                            <div className="input-group mb-3">
                                <span className="input-group-text">code</span>
                                <div className="form-floating">
                                    <input type="text" className="form-control-plaintext border border-primary" id="floatingPlaintextInput" placeholder="*****" />
                                </div>
                            </div>
                        </div>

                        <div className="form-floating mb-3">
                            <button type="button" className="btn btn-warning mx-auto"><a href=".../pages/ChatPage">Accept invite and Join Chat</a></button>

                        </div>


                    </div>
                </form>

            </div>
        </>
    );
}

export default ReceiverForm