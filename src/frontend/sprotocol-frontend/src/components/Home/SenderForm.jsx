function SenderForm() {

    const generateCode = () => {
    };
    return (
        <>
            <div className="sender-class ">

                <form action="" method="POST">
                    <div className="form-floating mb-3">
                        <input type="text" className="form-control" id="floatingInput" placeholder="..." />
                        <label htmlFor="floatingInput">Your Name</label>

                        <div className="d-inline-flex gap-3 m-2 form-floating">
                            <div className="input-group mb-3">
                                <span className="input-group-text"><button type="button" className="btn btn-outline-warning" onClick={generateCode}>generate code</button>
                                </span>

                                <input className="form-control" type="text" value="" placeholder="copy the code " aria-label="readonly input example" readOnly />

                            </div>
                        </div>

                        <div className="form-floating mb-3">
                            <button type="button" className="btn btn-success mx-auto">Join Chat</button>

                        </div>


                    </div>
                </form>

            </div>



        </>
    );
}

export default SenderForm


