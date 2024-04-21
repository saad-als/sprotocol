import { useState } from "react";
function SenderForm() {


    const [showLogin, setLogin] = useState(false);
    // const [userName, setUserName] = useState("");

    const handleLogin = (e) => {
        if (e) {
            return (<>
                <div className="d-inline-flex gap-3 m-2 form-floating">
                    <div className="input-group mb-3">


                        <input className="form-control" type="text" value="" placeholder="copy the code " aria-label="readonly input example" readOnly />

                    </div>
                </div>

                <div className="form-floating mb-3">
                    <button type="button" className="btn btn-success mx-auto">Join Chat</button>
                    {/* <p>{userName || 'no usrname'}</p> */}

                </div>

            </>)
        }
        else {
            return (
                <>
                    <div className="d-inline-flex form-floating mb-3">
                        <input type="text" className="form-control" id="floatingInput" placeholder="..." />
                        <label htmlFor="floatingInput">Your Name</label>
                        <span className="input-group-text">
                            <button type="submit" onClick={() => { setLogin(true) }} className="btn btn-outline-warning" >generate code</button>
                        </span>



                    </div>


                </>
            );
        }
    };


    return (
        <>
            <div className="sender-class ">

                <form action="" method="POST">
                    {handleLogin(showLogin)}
                </form>

            </div>



        </>
    );
}

export default SenderForm


