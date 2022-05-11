<?php
// GENERATED CODE -- DO NOT EDIT!

namespace Ovm;

/**
 */
class OtazkyVaclavaMoravceClient extends \Grpc\BaseStub {

    /**
     * @param string $hostname hostname
     * @param array $opts channel options
     * @param \Grpc\Channel $channel (optional) re-use channel object
     */
    public function __construct($hostname, $opts, $channel = null) {
        parent::__construct($hostname, $opts, $channel);
    }

    /**
     * @param \Ovm\MoravecRequest $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     * @return \Grpc\UnaryCall
     */
    public function VaclavMoravec(\Ovm\MoravecRequest $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/ovm.OtazkyVaclavaMoravce/VaclavMoravec',
        $argument,
        ['\Ovm\Response', 'decode'],
        $metadata, $options);
    }

    /**
     * @param \Ovm\KlausRequest $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     * @return \Grpc\UnaryCall
     */
    public function VaclavKlaus(\Ovm\KlausRequest $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/ovm.OtazkyVaclavaMoravce/VaclavKlaus',
        $argument,
        ['\Ovm\Response', 'decode'],
        $metadata, $options);
    }

    /**
     * @param \Ovm\ZemanRequest $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     * @return \Grpc\UnaryCall
     */
    public function MilosZeman(\Ovm\ZemanRequest $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/ovm.OtazkyVaclavaMoravce/MilosZeman',
        $argument,
        ['\Ovm\Response', 'decode'],
        $metadata, $options);
    }

}
