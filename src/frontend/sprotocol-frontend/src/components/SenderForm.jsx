function SenderForm() {
    return (
        <>
            <div className="sender-class ">

                <form action="">
                    <div className="form-floating mb-3">
                        <input type="text" className="form-control" id="floatingInput" placeholder="..." />
                        <label htmlFor="floatingInput">Your Name</label>

                        <div className="d-inline-flex gap-3 m-2 form-floating">
                            <div className="input-group mb-3">
                                <span className="input-group-text"><button type="button" className="btn btn-outline-warning">generate code</button>
                                </span>
                                <div className="form-floating">
                                    <input type="text" readOnly className="form-control-plaintext border border-primary" id="floatingPlaintextInput" placeholder="*****" />
                                    {/* <label htmlFor="floatingInputGroup1">Secure Code</label> */}
                                </div>
                            </div>
                        </div>
                    </div>
                </form>

            </div>



        </>
    );
}

export default SenderForm


