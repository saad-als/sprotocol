import SenderForm from "./SenderForm";
import ReceiverForm from "./RecevierForm";
import { useState } from "react";
function LoginForm() {
    const [value, setValue] = useState(null);
    return (
        <>

            <div className="container-fluid align-items-center justify-content-center rounded w-20">

                <div className="d-block text-center">
                    <img src="./././assets/sprotocol-logos/sprotocol-logos_black.png" alt="logo" className=" rounded d-block mx-auto" width="190" height="190" />
                    <h5 className="d-block">Welcome to [sprotocol] a secure web chat application</h5>
                    <p>are you sender or recevier?</p>
                </div>




                <div className="container-sm p-2 d-block text-center">
                    <div className="d-inline-flex gap-3 m-2">
                        <button className="btn btn-warning sender-btn" onClick={() => setValue(true)} type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
                            Sender
                        </button>

                        <button className="btn btn-success recevier-btn" onClick={() => setValue(false)} type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
                            Receiver
                        </button>

                    </div>

                    <div className="collapse p-1" id="collapseExample">
                        <div className="card card-body">

                            {value ? <SenderForm /> : <ReceiverForm />}

                        </div>
                    </div>


                </div>


            </div>
        </>
    );


}

export default LoginForm