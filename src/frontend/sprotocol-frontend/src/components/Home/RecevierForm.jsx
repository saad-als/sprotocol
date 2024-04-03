import { useState } from "react";
function ReceiverForm() {

    const [codeValue, checkCode] = useState(false);

    const handleCode = (e) => {
        if (e) {
            return (
                <>
                    <div className="form-floating mb-3">
                        <input type="text" className="form-control" id="floatingInput" placeholder="..." />
                        <label htmlFor="floatingInput">Your Name</label>

                        <div className="form-floating mb-3">
                            <button type="button" className="btn btn-success mx-auto">Accept invite and Join Chat</button>

                        </div>


                    </div>
                </>
            );

        } else {
            return (
                <>
                    <div className="form-floating mb-3">

                        <div className="d-inline-flex gap-3 m-2 form-floating">
                            <div className="input-group mb-3">
                                <span className="input-group-text">paste the code here</span>
                                <div className="form-floating">
                                    <input type="text" className="form-control-plaintext border border-primary" id="floatingPlaintextInput" placeholder="*****" />
                                </div>
                            </div>
                        </div>

                        <div className="form-floating mb-3">
                            <button type="button" className="btn btn-warning mx-auto" onClick={() => { checkCode(true) }}>check code & Next</button>

                        </div>


                    </div>

                </>
            );
        }

    };
    return (
        <>
            <div className="recevier-class">

                <form action="">

                    {handleCode(codeValue)}
                </form>

            </div>
        </>
    );
}

export default ReceiverForm