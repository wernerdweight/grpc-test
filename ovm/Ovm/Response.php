<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ovm.proto

namespace Ovm;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>ovm.Response</code>
 */
class Response extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>repeated .ovm.Sentence sentences = 1;</code>
     */
    private $sentences;
    /**
     * Generated from protobuf field <code>int32 score = 2;</code>
     */
    private $score = 0;

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type \Ovm\Sentence[]|\Google\Protobuf\Internal\RepeatedField $sentences
     *     @type int $score
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Ovm::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>repeated .ovm.Sentence sentences = 1;</code>
     * @return \Google\Protobuf\Internal\RepeatedField
     */
    public function getSentences()
    {
        return $this->sentences;
    }

    /**
     * Generated from protobuf field <code>repeated .ovm.Sentence sentences = 1;</code>
     * @param \Ovm\Sentence[]|\Google\Protobuf\Internal\RepeatedField $var
     * @return $this
     */
    public function setSentences($var)
    {
        $arr = GPBUtil::checkRepeatedField($var, \Google\Protobuf\Internal\GPBType::MESSAGE, \Ovm\Sentence::class);
        $this->sentences = $arr;

        return $this;
    }

    /**
     * Generated from protobuf field <code>int32 score = 2;</code>
     * @return int
     */
    public function getScore()
    {
        return $this->score;
    }

    /**
     * Generated from protobuf field <code>int32 score = 2;</code>
     * @param int $var
     * @return $this
     */
    public function setScore($var)
    {
        GPBUtil::checkInt32($var);
        $this->score = $var;

        return $this;
    }

}

