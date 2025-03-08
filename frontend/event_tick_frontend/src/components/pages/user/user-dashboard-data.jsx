
import styles from './user.module.css'


import PropTypes from 'prop-types';

export default function UserDashboardData({lable1, lable1Data, lable2, lable2Data, lable3, lable3Data,lable4, lable4Data, }) {
  return (
    <>
    <section className={styles.circle__notice}>
            <div>
              {lable1}
              <span>{lable1Data}</span>
            </div>
            <div>
              {lable2}
              <span>{lable2Data}</span>
            </div>
            <div>
              {lable3}
              <span>{lable3Data}</span>
            </div>
            <div>
              {lable4}
              <span>{lable4Data}</span>
            </div>
          </section>

    </>
  );
}
export const TableData =()=>{
    return (
        <>
         <tr>
              <td>eeeeeeeeee</td>
              <td>aaaaaaaaaaatttt</td>
              <td>sssssssst</td>
              <td>eeeeeeeeed</td>
              <td>ddddddddy</td>
              <td>bbbbbbbbl</td>
              <td>sssssssssssst</td>
          </tr>   
        </>
    )

}
UserDashboardData.propTypes = {
    lable1: PropTypes.string.isRequired,
    lable1Data: PropTypes.string.isRequired,
    lable2: PropTypes.string.isRequired,
    lable2Data: PropTypes.string.isRequired,
    lable3: PropTypes.string.isRequired,
    lable3Data: PropTypes.string.isRequired,
    lable4: PropTypes.string.isRequired,
    lable4Data: PropTypes.string.isRequired,
    
};


